=====
Gallery
=====

Gallery is a simple Django app/plugin to handle Web-based photo-albums. Users can
create photo collections and easy display the in the front end

Detailed documentation is in the "docs" directory.

Quick start
-----------
## Use it as a Django third party application
1. Add "gallery" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'gallery',
    ]

2. Include the gallery URLconf in your project urls.py like this::

    url(r'^gallery/', include('gallery.urls')),

3. Run `python manage.py migrate gallery` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a gallery (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/gallery/ to vie the list of galleries you just created.

## Use it as a Django CMS plugin
TODO: Complete instructions

pip install --upgrade git+http://git@github.com/GoWebyCMS/gallery.git