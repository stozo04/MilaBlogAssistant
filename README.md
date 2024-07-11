# Mila Blog Helper

This is a Python script to help automate the creation and updating of blog entries for Mila's blog.

## Script: blog-assistant.py

### Description

The `blog-assistant.py` script automates the process of creating a new blog entry based on a template and appending the new entry to the `blog-list.html`.

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
   - `Enter file name (e.g., blog-one-year-one-months): `
   - `Enter the date (e.g., July 30, 2023): `
   - `Enter Mila's age (e.g., 1 year 1 month): `

### Script Details

#### `update_blog(htmlFile, date, age)`

- **Parameters:**

  - `htmlFile`: The file name for the new blog post.
  - `date`: The date of the blog post.
  - `age`: Mila's age for the blog post.

- **Functionality:**
  - Reads the `blog-template.html`.
  - Replaces the placeholders (`{{date}}`, `{{age}}`) with the provided inputs.
  - Writes the new blog content to a new HTML file.
  - Calls `append_to_blog_list` to update `blog-list.html`.

#### `append_to_blog_list(blog_list_path, date, age, blog_path)`

- **Parameters:**

  - `blog_list_path`: The path to the blog list file.
  - `date`: The date of the blog post.
  - `age`: Mila's age for the blog post.
  - `blog_path`: The path to the new blog post file.

- **Functionality:**
  - Generates a new blog entry HTML.
  - Appends the new entry to `blog-list.html`.

## Example

After running the script and providing the necessary inputs, a new blog post will be created and the blog list will be updated accordingly.

### Template File (`blog-template.html`)

Ensure your `blog-template.html` includes placeholders for `{{date}}` and `{{age}}`.

### Blog List File (`blog-list.html`)

Ensure your `blog-list.html` file exists and is in the correct format to receive new entries.

### Contact

For any questions or further assistance, feel free to reach out.

Happy blogging!
