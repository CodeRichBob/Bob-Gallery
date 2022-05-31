# GALLERY

## Project Description

Gallery is a Photo Gallery application showcasing a collection of pictures built using Python - Django.

- Users get can view photos uploaded by admin.
- Users can see photos based on the location, by clicking on the listed locations in the menu.
- They can also copy the link to a photo to paste at their discretion.
- Users can search for photos based on categories.

## BDD

| Behavior                     | Input                                          | Output                                                                |
| ---------------------------- | ---------------------------------------------- | --------------------------------------------------------------------- |
| View photos of interest      | Scroll to see a gallery and click on picture   | Displays a picture with name description and copy link for sharing    |
| Search a picture by category | Enter the category in the search input         | Displays Images in the searched category                              |
| View pictures by location    | Click on location of interest from the Navbar  | Displays Images of chosen location                                    |
| Copy Link to clipboard       | Click on copy link button in the modal class   | Copies link to clipboard                                              |
| View Single picture          | Click on photo of interest then click on image | Displays a single page with details of the picture and related images |

<br>

## Getting Started

To clone the repository, run:

    git clone https://github.com/CodeRichBob/Bob-Gallery.git

Then navigating to the cloned directory:

    cd Bob-Gallery

### Prerequisite

The Galleria project requires a prerequisite understanding of the following:

- Django Framework
- Python3.9
- Postgres
- Python virtualenv
