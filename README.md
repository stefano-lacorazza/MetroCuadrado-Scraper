
### Selenium and BS4 based scraper for [www.metrocuadrado.com](https://www.metrocuadrado.com/)
---


## Config


* Install the requirements.
    * ```pip install -r requirements```

## Directory Structure

<br>

* ```./dependencies``` "Saves all the scripts referenced by the file  ```main.py``` 

    *  ```./dependencies/geturls.py``` Code segment specifically dedicated to extracting specific URLs from all the posts on the given page

    * ```./dependencies/clean.py``` Code segment specifically dedicated to removing duplicate and irrelevant data that has been returned by the previous part.

    * ```./dependencies/getdetails.py``` pCode segment specifically dedicated to returning the details of a specific post and adding them to the file. ```csv``` in ```./logs```

<br>

*  ```./logs``` Saves the files with necessary data for scraping
    *  ```./logs/frame.csv``` CSV file where all the publication data are saved.
    *  ```./logs/urls.json``` JSON file that stores all the URLs to specific publications

    *   ```./logs/urls_cleaned.json``` JSON file that stores all the data of ```./logs/urls.json```.
## Functions
* ```get```
    * Creates the ```urls.json``` file containing all the URLs from the webpage that is passed as a parameter to this function.
*``` clean```
    *  Filters the ```urls.json``` file in order to remove all duplicate results. This function will create the  ```urls_cleaned.json``` file
* ```Scrape```
    * Extracts all the data from the records in the  ```urls_cleaned.json```, file and add them to the file ```frame.csv```

## Usage
* Extract the desired URL from  [www.metrocuadrado.com](https://www.metrocuadrado.com/)
    * SSelect the first two search criteria from the different dropdown menus.
    * Input the third criteria and click on the "Search" button.
    * Copy the URL from the browser's address bar.

<br>


* Function ```get```
    * From the project directory, execute the following command:
        
        *  ```python main.py get [url]```
        * Example:
            *  ```python main.py get www.metrocuadrado.com/apartamentos-casas/venta/bogota/```
    * Once this process is complete, the information will be reflected in the file:
```./logs/urls.json```  

<br>

* Function ```clean```
    *  From the project directory, execute the following command: 
        * ```python main.py clean```
    * Once this process is complete, the information will be reflected in the file:
```./logs/urls_cleaned.json```

<br>


* Function ```scrape```
    * From the project directory, execute the following command: 
        *  ```python main.py scrape [true/false]```
            * The parameters ```true / false``` hacen referencia al uso de la ```API``` refer to the usage of the Google geocoding API.
    * 
At the end of this process, the information will be reflected in the file.
```./logs/frame.csv```

