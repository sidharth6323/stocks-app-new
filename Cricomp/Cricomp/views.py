from django.shortcuts import render, render_to_response, HttpResponse, RequestContext
import urllib
import json
from bs4 import BeautifulSoup
import re

def base(request):
	return render_to_response("base.html",{})

def index(request):
	return render_to_response("index.html",{})

def signup(request):
	return render_to_response("signup.html",{})

