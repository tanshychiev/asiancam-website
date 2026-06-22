from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CompanyNewsForm
from .models import CompanyNews, CompanyNewsPhoto


def is_admin_or_staff(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)


# =========================
# Public Website Pages
# =========================

def home(request):
    latest_news = (
        CompanyNews.objects
        .filter(is_published=True)
        .order_by("-sort_order", "-created_at")[:3]
    )

    return render(request, "index.html", {
        "latest_news": latest_news,
    })


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")


def clients(request):
    return render(request, "clients.html")


def certificates(request):
    return render(request, "certificates.html")


def staff(request):
    return render(request, "staff.html")


def contact(request):
    return render(request, "contact.html")


def news_detail(request, news_id):
    news = get_object_or_404(
        CompanyNews.objects.prefetch_related("photos"),
        id=news_id,
        is_published=True,
    )

    return render(request, "news_detail.html", {
        "news": news,
    })


# =========================
# Admin / Dashboard Pages
# =========================

@login_required
@user_passes_test(is_admin_or_staff)
def dashboard_news_list(request):
    news_list = (
        CompanyNews.objects
        .all()
        .order_by("-sort_order", "-created_at")
    )

    return render(request, "dashboard_news_list.html", {
        "news_list": news_list,
    })


@login_required
@user_passes_test(is_admin_or_staff)
def dashboard_news_add(request):
    if request.method == "POST":
        form = CompanyNewsForm(request.POST, request.FILES)

        if form.is_valid():
            news = form.save()

            gallery_images = request.FILES.getlist("gallery_images")
            for img in gallery_images:
                CompanyNewsPhoto.objects.create(news=news, photo=img)

            messages.success(request, "News uploaded successfully.")
            return redirect("dashboard_news_list")
    else:
        form = CompanyNewsForm()

    return render(request, "dashboard_news_add.html", {
        "form": form,
        "is_edit": False,
    })


@login_required
@user_passes_test(is_admin_or_staff)
def dashboard_news_edit(request, news_id):
    news = get_object_or_404(
        CompanyNews.objects.prefetch_related("photos"),
        id=news_id,
    )

    if request.method == "POST":
        form = CompanyNewsForm(request.POST, request.FILES, instance=news)

        if form.is_valid():
            news = form.save()

            delete_photo_ids = request.POST.getlist("delete_photos")
            if delete_photo_ids:
                CompanyNewsPhoto.objects.filter(
                    id__in=delete_photo_ids,
                    news=news,
                ).delete()

            gallery_images = request.FILES.getlist("gallery_images")
            for img in gallery_images:
                CompanyNewsPhoto.objects.create(news=news, photo=img)

            messages.success(request, "News updated successfully.")
            return redirect("dashboard_news_list")
    else:
        form = CompanyNewsForm(instance=news)

    return render(request, "dashboard_news_add.html", {
        "form": form,
        "news": news,
        "is_edit": True,
    })


@login_required
@user_passes_test(is_admin_or_staff)
def dashboard_news_delete(request, news_id):
    news = get_object_or_404(CompanyNews, id=news_id)

    if request.method == "POST":
        news.delete()
        messages.success(request, "News deleted successfully.")
        return redirect("dashboard_news_list")

    return render(request, "dashboard_news_delete.html", {
        "news": news,
    })