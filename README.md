# Data Visualization Lab Assignments
##### The data sets used for the assignments have been listed below.
#
### dvlab1.py
Use the following data, and plot the graphs using matplotlib library.  
data = [['E001', 'M', 34, 123, 'Normal', 350],  
        ['E002', 'F', 40, 114, 'Overweight', 450],  
        ['E003', 'F', 37, 135, 'Obesity', 169],  
        ['E004', 'M', 30, 139, 'Underweight', 189],  
        ['E005', 'F', 44, 117, 'Underweight', 183],  
        ['E006', 'M', 36, 121, 'Normal', 80],  
        ['E007', 'M', 32, 133, 'Obesity', 166],  
        ['E008', 'F', 26, 140, 'Normal', 120],  
        ['E009', 'M', 32, 133, 'Normal', 75],  
        ['E010', 'M', 36, 133, 'Underweight', 40] ]    
df = pd.DataFrame(data, columns = ['EMPID', 'Gender', 'Age', 'Sales', 'BMI', 'Income'] )  
For all the plots include title, x-axis label, y-axis label, color, and legend.  

### dvlab2.py
a) Using stacked bar chart to show the confirmed Indian and foreign national cases for the state Kerala and Tamil Nadu for a period of 1 week.  
b) Use a table and show the data for cured and deaths in April to three states with mean, variance and correlation showing in the bottom of the table.  
c) Explore the structure of the data considered in problem 2 using appropriate visual representations.  
Dataset – Covid-19 Indian dataset from Kaggle  
https://www.kaggle.com/sudalairajkumar/covid19-in-india

### dvlab3.py
Dataset - For height and weight plot take any random 20 values of your choice

### dvlab4.py
Create a file using the attributes Aadhar number, Name, Date of birth, age, temperature, RTPCR result, vaccinated, phone, State, country with 50 entries of your own.  
Use the following attribute semantics and encode the data using different colours.  
1) Display the data as table and distinguish Multivariate/Multidiamensial table  
2) Key attributes and valued attributes  
3) Quantitative data, categorical data  
Sequential ordering, diverging ordering and cyclic ordering

### dvlab5.py
For the given situation identify an abstract level task. Associate suitable abstract dataset and datatype with the task. Design a visual idiom with minimum two visualization techniques to realize the task. Include title, axis labelling, legends and colour encodings in the charts. Prepare a document for submission including the details, code and output snapshot.  
Domain “Natural Farming”  
9) Explore the Nutrient absorption by the crops, natural fertilizer usage and yield in natural farming  
Dataset stored as a CSV file and then uploaded.  
Data used to analyse and display the different fertilizers used, the nutrients absorbed and the yield produced.  

### dvlab6.py
Design a bivariate colormap for the attributes animals and their presence. Attibute Animal : Tiger, Elephant,Lion Attribute : Presence : 1, 0. Use the designed color map to encode the data given in the table over a map.  
![image](https://user-images.githubusercontent.com/81374415/130357587-bc943ee2-85ec-4552-851e-eb1a95844a05.png)

### dvlab7.py
For the table data given below, design a visual idiom to understand the spread of values using the attributes CGPA, Btech Program and Gender. Use marks and other channels in the idiom.  
![image](https://user-images.githubusercontent.com/81374415/130357617-e038c835-968f-41d6-a524-eaa95d3cbfa0.png)

### dvlab8.py
For the given road network data, design visual idioms to show the node-edge diagram using force directed placement method and vertical top-down placement method. Apply color and other channels to encode the distance and safety attributes in the idioms. Distinguish longest and shortest safety paths through appropriate visual encodings. 

### dvlab9.py
- Data visualization for the total profit data for each month.
- Data visualization for number of units sold per month for each product.
- Data visualization for the product sales using stack plot.
