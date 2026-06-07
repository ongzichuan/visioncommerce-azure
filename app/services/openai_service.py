def generate_listing(product_name, category, image_analysis):
    return f"""
Product Title:
{product_name} | Quality {category} Product

Short Description:
A clean and marketplace-ready listing generated from the uploaded product image.

Key Selling Points:
- Clear product presentation
- Suitable for Shopee and Lazada sellers
- AI Vision analysed image tags and caption
- Simple and readable product copy
- Useful for small e-commerce sellers

Shopee/Lazada Listing Copy:
Introducing {product_name}, a {category} product prepared for online marketplace listing.

Image Analysis Used:
{image_analysis}
"""