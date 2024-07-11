import os

def update_blog(htmlFile, date, age):
    template_path = 'D:\\Personal\\milagates\\Mila\\blogs\\blog-template.html'
    output_path = f'D:\\Personal\\milagates\\Mila\\blogs\\{htmlFile}.html'
    blog_list_path = 'D:\\Personal\\milagates\\Mila\\blogs\\blog-list.html'
    
    if not os.path.exists(template_path):
        print(f"Oops! The template file {template_path} does not exist.")
        return
    
    with open(template_path, 'r') as file:
        content = file.read()
    
    content = content.replace('{{date}}', date)
    content = content.replace('{{age}}', age)
    
    with open(output_path, 'w') as file:
        file.write(content)
    
    print(f"Yay! Your blog for {date} has been created: {output_path}")
    
    # Append the new blog entry to the blog list
   #  append_to_blog_list(blog_list_path, date, age, output_path)

def append_to_blog_list(blog_list_path, date, age, blog_path):
    if not os.path.exists(blog_list_path):
        print(f"Oops! The blog list file {blog_list_path} does not exist.")
        return
    
    # Generate the new blog entry HTML
    blog_entry = f'''
    <!-- Blog {age} -->
    <div class="cbp-item 2024 new">
        <a href="./{os.path.basename(blog_path)}" class="cbp-caption">
            <div class="cbp-caption-defaultWrap">
                <img src="../assets/images/TODO/1.jpg" alt="">
            </div>
            <div class="cbp-caption-activeWrap">
                <div class="cbp-l-caption-alignCenter">
                    <div class="cbp-l-caption-body">
                        <div class="cbp-l-caption-text">VIEW POST</div>
                    </div>
                </div>
            </div>
        </a>
        <div class="cbp-l-grid-blog-title">{age} Letter</div>
        <div class="cbp-l-grid-blog-date">{date}</div>
    </div>
    '''
    
    with open(blog_list_path, 'a') as file:
        file.write(blog_entry)
    
    print(f"Yay! Your blog list has been updated with the new blog for {date}.")

if __name__ == "__main__":
    htmlFile = input("Enter file name (e.g., blog-one-year-one-months): ")
    date = input("Enter the date (e.g., July 30, 2023): ")
    age = input("Enter Mila's age (e.g., 1 year 1 month): ")
    update_blog(htmlFile, date, age)
