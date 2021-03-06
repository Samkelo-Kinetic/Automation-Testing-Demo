# -*- coding: utf-8 -*-
u"""
Copyright 2015 Telefónica Investigación y Desarrollo, S.A.U.
This file is part of Toolium.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from behave import given, when, then

from android_behave.pageobjects.menu import MenuPageObject
from android_behave.pageobjects.views import  ViewsPageObject

@given('the menu page is open')
def step_impl(context):
    context.current_page = ViewsPageObject()

@when('the user clicks views')
def step_impl(context):
	context.current_page = ViewsPageObject()
	context.current_page.view_btn()

@when('clicks Animation')
def step_impl(context):
	context.current_page = ViewsPageObject()
	context.current_page.animation_btn()

@when('clicks 3D Transition')
def step_impl(context):
	context.current_page = ViewsPageObject()
	context.current_page.trans_btn()

@then('clicks lyon')
def step_impl(context):
	context.current_page = ViewsPageObject()
	context.current_page.lyon_btn()