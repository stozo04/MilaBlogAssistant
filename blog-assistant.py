import os
import shutil
import re
from datetime import datetime

# Helper function to convert numbers to words (for 0 to 10)
def number_to_words(number):
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    return words[number] if 0 <= number <= 10 else str(number)

def create_blog_entries(date, age, myJourneyFileName, blog_output_path, journey_output_path, blog_template_path, journey_template_folder, journey_list_path):
    # Create Blog entry
    if not os.path.exists(blog_template_path):
        print(f"Oops! The blog template file {blog_template_path} does not exist.")
        return
    
    with open(blog_template_path, 'r') as file:
        content = file.read()
    
    content = content.replace('{{date}}', date)
    content = content.replace('{{age}}', age)
    
    with open(blog_output_path, 'w') as file:
        file.write(content)
    
    print(f"Yay! Your blog for {date} has been created: {blog_output_path}")
    
    # Append the new blog entry to the blog list
    append_to_blog_list(blog_list_path='D:\\Personal\\milagates\\Mila\\blogs\\blog-list.html', date=date, age=age, blog_path=blog_output_path)
    
    # Create My Journey entry
    create_myJourney_folder(myJourneyFileName, journey_template_folder)
    append_to_my_journey_list(journey_list_path, age, myJourneyFileName, journey_output_path)

def append_to_blog_list(blog_list_path, date, age, blog_path):
    if not os.path.exists(blog_list_path):
        print(f"Oops! The blog list file {blog_list_path} does not exist.")
        return
    
    # Convert the year portion to words for the image path
    years = int(age.split()[0])  # Extract the numeric year value
    year_word = number_to_words(years)  # Convert to word form, e.g., "1" -> "one"
    myJourneyFileName = blog_path.split("\\")[-1].replace("blog-", "").replace(".html", "")  # Extract "one-year-five-months"
    
    # Define dynamic image path based on age and file structure
    image_path = f"../assets/images/birthday/{year_word}-year/{myJourneyFileName}/1.jpg"
    
    # Generate the new blog entry HTML with the updated image path
    blog_entry = f'''
    <!-- Blog {age} -->
    <div class="cbp-item 2024 new">
        <a href="./one-year/{os.path.basename(blog_path)}" class="cbp-caption">
            <div class="cbp-caption-defaultWrap">
                <img src="{image_path}" alt="">
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
    # Determine the folder path based on the year
    year_word = myJourneyFileName.split("-")[0]  # Extract year in words (e.g., "one")
    new_folder_path = f'D:\\Personal\\milagates\\Mila\\my-journey\\{year_word}-year\\{myJourneyFileName}'
    
    # Create the folder if it doesn't exist
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)
        print(f"Created new folder: {new_folder_path}")
    
    # Define paths to the templates
    template_html = os.path.join(template_folder, 'template.html')
    template_load_more_html = os.path.join(template_folder, 'template-load-more.html')
    
    # Define paths for the new files
    new_html_path = os.path.join(new_folder_path, f'{myJourneyFileName}.html')
    new_load_more_html_path = os.path.join(new_folder_path, f'{myJourneyFileName}-load-more.html')
    
    # Read and customize the template content
    with open(template_html, 'r') as file:
        content = file.read()
    
    # Replace placeholder with `myJourneyFileName`
    content = content.replace('{{loadMoreHTML}}', myJourneyFileName)
    
    # Write main HTML file
    with open(new_html_path, 'w') as file:
        file.write(content)
    
    # Copy the load-more template without modifications
    shutil.copy(template_load_more_html, new_load_more_html_path)
    
    print(f"Copied and renamed template files to {new_folder_path} with placeholders replaced")


def append_to_my_journey_list(journey_list_path, age, myJourneyFileName, journey_output_path):
    if not os.path.exists(journey_list_path):
        print(f"Oops! The journey list file {journey_list_path} does not exist.")
        return
    
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
    
    with open(journey_list_path, 'a') as file:
        file.write(myJourney_entry)
    
    print(f"Yay! Your My Journey has been updated with the new event for {age}.")


# Predict and Confirm Autofill Values
def predict_values(input_text):
    # Match input pattern for age
    match = re.search(r'(\d+)\s*year(?:s)?(?:\s+and\s+)?(\d+)?\s*month(?:s)?', input_text, re.IGNORECASE)
    if match:
        years = int(match.group(1))
        months = int(match.group(2) or 0)  # Default to 0 if months are omitted
        
        # Convert numbers to words for paths and names
        year_word = number_to_words(years)
        month_word = number_to_words(months)
        age = f"{years} Year{'s' if years > 1 else ''} {months} Month{'s' if months > 1 else ''}"
        myJourneyFileName = f"{year_word}-year-{month_word}-months"
        
        # Construct Blog paths
        blog_folder = f"D:\\Personal\\milagates\\Mila\\blogs\\{year_word}-year"
        blog_output_path = os.path.join(blog_folder, f"blog-{myJourneyFileName}.html")
        
        # Construct My Journey paths
        journey_template_folder = f'D:\\Personal\\milagates\\Mila\\my-journey\\{year_word}-year\\template'
        journey_output_path = f'D:\\Personal\\milagates\\Mila\\my-journey\\{year_word}-year\\{myJourneyFileName}\\{myJourneyFileName}.html'
        journey_list_path = f'D:\\Personal\\milagates\\Mila\\my-journey\\{year_word}-year\\{year_word}-year-journey.html'
        
        # Use a fixed blog template path
        blog_template_path = 'D:\\Personal\\milagates\\Mila\\blogs\\blog-template.html'
        
        # Default to current date
        date = datetime.now().strftime("%B %d, %Y")
        return date, age, myJourneyFileName, blog_output_path, journey_output_path, blog_template_path, journey_template_folder, journey_list_path
    else:
        print("Invalid format. Please enter a phrase like '1 Year and 5 Months'")
        return None, None, None, None, None, None, None, None


def confirm_value(prompt, value):
    user_input = input(f"{prompt} is '{value}'. Press Enter to confirm or type a new value: ")
    return user_input if user_input else value

# Main execution block
if __name__ == "__main__":
    input_text = input("Enter Mila's age (e.g., '1 Year and 5 Months'): ")
    date, age, myJourneyFileName, blog_output_path, journey_output_path, blog_template_path, journey_template_folder, journey_list_path = predict_values(input_text)

    # Confirm each value, grouped logically
    # General
    date = confirm_value("Date", date)
    age = confirm_value("Age", age)
    
    # My Journey Fields
    myJourneyFileName = confirm_value("My Journey File Name", myJourneyFileName)
    journey_output_path = confirm_value("My Journey Output Path", journey_output_path)
    journey_template_folder = confirm_value("My Journey Template Folder Path", journey_template_folder)
    journey_list_path = confirm_value("Journey List Path", journey_list_path)
    
    # Blog Fields
    blog_output_path = confirm_value("Blog Output Path", blog_output_path)
    blog_template_path = confirm_value("Blog Template Path", blog_template_path)

    # Create the blog and My Journey entries
    create_blog_entries(date, age, myJourneyFileName, blog_output_path, journey_output_path, blog_template_path, journey_template_folder, journey_list_path)
