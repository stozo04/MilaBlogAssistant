
# Mila Blog Helper

This Python script automates the creation and updating of blog entries for Mila's blog, creating both “Blog” and “My Journey” entries in a structured format based on Mila's age.

## Script: blog-assistant.py

### Description

The `blog-assistant.py` script automates the process of creating new blog entries and journey entries based on templates. It dynamically generates paths based on Mila's age and appends the new entry to `blog-list.html` and `one-year-journey.html`.

### Usage

1. **Ensure the following files exist:**

   - `blog-template.html` in the `D:\Personal\milagates\Mila\blogs` directory.
   - `blog-list.html` in the `D:\Personal\milagates\Mila\blogs` directory.

2. **Run the script:**

   - Open a command prompt.
   - Navigate to the directory containing `blog-assistant.py`:
     ```sh
     cd D:\Personal\MilaBlogHelper
     ```
   - Run the script:
     ```sh
     python blog-assistant.py
     ```

3. **Provide the inputs when prompted:**
   - `Enter Mila's age (e.g., '1 Year and 5 Months'): `
   - Confirm each dynamically generated path and filename for Blog and My Journey files.

### Script Details

#### `create_blog_entries(date, age, myJourneyFileName, blog_output_path, journey_output_path, blog_template_path, journey_template_folder, journey_list_path)`

- **Parameters:**

  - `date`: The date of the blog post.
  - `age`: Mila's age for the blog post.
  - `myJourneyFileName`: The dynamic file name for the journey entry based on age.
  - `blog_output_path`: Path for the new blog HTML file.
  - `journey_output_path`: Path for the new journey HTML file.
  - `blog_template_path`: Path to the blog template file.
  - `journey_template_folder`: Path to the My Journey template folder.
  - `journey_list_path`: Path to the journey list file (e.g., `one-year-journey.html`).

- **Functionality:**
  - Reads and replaces placeholders in the `blog-template.html`.
  - Creates a new blog and journey HTML file in their respective folders.
  - Updates `blog-list.html` and the journey list file with the new entries.

### Dynamic Image Paths

The image paths are dynamically generated based on Mila's age, structured as:
```
<img src="../assets/images/birthday/{one-year}/{one-year-five-months}/1.jpg" alt="">
```
This structure is automatically generated when creating the blog entry.

### Example

After running the script and confirming each path, a new blog and journey entry will be created, and both lists will be updated.

### Template File (`blog-template.html`)

Ensure your `blog-template.html` includes placeholders for `{{date}}` and `{{age}}`.

### Blog List File (`blog-list.html`)

Ensure your `blog-list.html` file exists and is in the correct format to receive new entries.

### Contact

For any questions or further assistance, feel free to reach out.

Happy blogging!
