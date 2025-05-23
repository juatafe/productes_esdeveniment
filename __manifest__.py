{
    'name': 'Productes per a Esdeveniments',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Plantilles i tiquets vinculats a esdeveniments',
    'depends': ['event', 'product', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/event_views.xml',
        'views/product_views.xml',
        'views/menu_views.xml',
        'data/product_templates.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}