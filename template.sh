#!/bin/bash

# Create main project folder
mkdir -p blackcoffer_assignment


cd blackcoffer_assignment

echo "Creating project structure..."

touch blackcoffer_assignment.py

touch README.txt

mkdir -p StopWords
mkdir -p MasterDictionary
mkdir -p Articles

touch Input.xlsx

echo "Place all StopWords files inside: blackcoffer_assignment/StopWords/"
echo "Place all MasterDictionary files inside: blackcoffer_assignment/MasterDictionary/"
echo "Place Input.xlsx inside the project folder."
echo ""
echo "Project folder structure created successfully!"
echo ""


tree .
