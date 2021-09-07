from django.urls import path
from adminpanelapp import views

app_name = 'admin_app'

urlpatterns = [
    path('', views.adminindexview, name='adminindex'),
    path('all-user/', views.alluserview, name='all_user'),
    path('single-user/<str:user_pk>/', views.singleuserview, name='single_user'),
    path('single-user-edit/<str:user_pk>/', views.singleusereditview, name='single_user_edit'),
    path('order-details/', views.orderdetailsview, name='order_details'),
    path('order/', views.allorderview, name='order'),
    # Category URLS
    path('addcategories/', views.addcategoryview, name='add-categories'),
    path('valcategories/', views.validate_category, name='val-categories'),
    path('viewcategories/', views.viewcategoryview, name='view-categories'),
    path('deletecategories/<str:cat_pk>/', views.deletecategoryview, name='delete-categories'),
    path('editcategories/<str:cat_pk>/', views.editcategoryview, name='edit-categories'),

    path('addsubcategories/', views.addsubcategoryview, name='add-sub-categories'),
    path('viewsubcategories/', views.viewsubcategoryview, name='view-sub-categories'),
    path('deletesubcategories/<str:sub_cat_pk>/', views.deletesubcategoryview, name='delete-sub-categories'),
    path('editsubcategories/<str:sub_cat_pk>/', views.editsubcategoryview, name='edit-sub-categories'),

    path('addmanufacturer/', views.addmanufacturerview, name='add-manufacturer'),
    path('valmanufacturer/', views.validate_manufacturer, name='val-manufacturer'),
    path('viewmanufacturer/', views.viewmanufaturerview, name='view-manufacturer'),
    path('deletecompany/<str:man_pk>/', views.deletemanufacturerview, name='delete-company'),
    path('editcompany/<str:man_pk>/', views.editmanufacturerview, name='edit-company'),

    path('allproducts/', views.allproductsview, name='all-products'),
    path('subcategorydropdown/', views.load_subcategories, name='subcategory-dropdown'),
    path('addproducts/', views.addproductsview, name='add-products'),
    path('editproducts/<int:product_pk>', views.editproductsview, name='edit-products'),
    path('deleteproducts/<int:product_pk>', views.deleteproductsview, name='delete-products'),
    path('editproductsimages/<int:product_pk>', views.editproductsimageview, name='edit-products-images'),

    path('addcoupons/', views.addcouponview, name='add-coupons'),
    path('viewcoupons/', views.viewcouponview, name='view-coupons'),
    path('valcoupons/', views.validate_coupons, name='val-coupons'),
    path('deletecoupons/<str:coupon_pk>/', views.deletecouponsview, name='delete-coupons'),
    path('editcoupons/<str:coupon_pk>/', views.editcouponsview, name='edit-coupons'),

    path('adminlogin/', views.adminloginview, name='admin-login'),
    path('adminlogout/', views.adminlogoutview, name='admin-logout'),
]