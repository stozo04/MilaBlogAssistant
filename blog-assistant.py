import os
import shutil

def create_blog(bloglFileName, date, age, myJourneyFileName):
    template_path = 'D:\\Personal\\milagates\\Mila\\blogs\\blog-template.html'
    output_path = f'D:\\Personal\\milagates\\Mila\\blogs\\one-year\\{bloglFileName}.html'
    blog_list_path = 'D:\\Personal\\milagates\\Mila\\blogs\\blog-list.html'
    template_folder = 'D:\\Personal\\milagates\\Mila\\my-journey\\one-year\\template'
    one_year_journey_list_path = 'D:\\Personal\\milagates\\Mila\\my-journey\\one-year\\one-year-journey.html'

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
    append_to_blog_list(blog_list_path, date, age, output_path)
    
    # Create new folder and copy template files
    create_myJourney_folder(myJourneyFileName, template_folder)

    # Append to One Year Journey list page
    append_to_my_journey_list(one_year_journey_list_path, age, myJourneyFileName)

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

def create_myJourney_folder(myJourneyFileName, template_folder):
    new_folder_path = f'D:\\Personal\\milagates\\Mila\\my-journey\\one-year\\{myJourneyFileName}'
    
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)
        print(f"Created new folder: {new_folder_path}")
    
    template_html = os.path.join(template_folder, 'template.html')
    template_load_more_html = os.path.join(template_folder, 'template-load-more.html')
    
    new_html_path = os.path.join(new_folder_path, f'{myJourneyFileName}.html')
    new_load_more_html_path = os.path.join(new_folder_path, f'{myJourneyFileName}-load-more.html')
    
    with open(template_html, 'r') as file:
        content = file.read()
    
    content = content.replace('{{loadMoreHTML}}', myJourneyFileName)
    
    with open(new_html_path, 'w') as file:
        file.write(content)

    # Ensure the load more template file is copied without modifications
    shutil.copy(template_load_more_html, new_load_more_html_path)
    
    print(f"Copied and renamed template files to {new_folder_path} with placeholders replaced")

def append_to_my_journey_list(one_year_journey_list_path, age, myJourneyFileName):
    if not os.path.exists(one_year_journey_list_path):
        print(f"Oops! The blog list file {one_year_journey_list_path} does not exist.")
        return
    
    # Generate the new blog entry HTML
    myJourney_entry = f'''
    <!-- {age} -->
    <div class="row m-t-20 cbp-item" style="padding-top: 1rem;">                                        
        <div class="pricing" style="width: 90%!important;">
            <h3>{age}</h3>
            <div class="pricing-price">
                TODO
            </div>
            <div class="btn-container" style="margin-top: 2rem;">
                <a href="./{myJourneyFileName}/{myJourneyFileName}.html">View</a>
            </div>
        </div>                                        
    </div>
    '''
    
    with open(one_year_journey_list_path, 'a') as file:
        file.write(myJourney_entry)
    
    print(f"Yay! Your My Journey has been updated with the new event for {age}.")

if __name__ == "__main__":
    bloglFileName = input("Enter Blog file name (e.g., blog-one-year-one-month(s)): ")
    date = input("Enter the date (e.g., July 30, 2023): ")
    age = input("Enter Mila's age (e.g., 1 Year 1 Month(s)): ")
    myJourneyFileName = input("Enter My Journey File Name (e.g., one-year-one-month): ")
    create_blog(bloglFileName, date, age, myJourneyFileName)
