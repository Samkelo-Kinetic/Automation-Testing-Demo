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
from android_behave.pageobjects.messaging import  MessagingPageObject


@given('the menu is already open')
def step_impl(context):
    context.current_page = MenuPageObject()


@when('the user clicks OS button')
def step_impl(context):
	context.current_page = MessagingPageObject()
	context.current_page.os_btn()

@when('clicks the sms messaging option')
def step_impl(context):
	context.current_page = MessagingPageObject()
	context.current_page.sms_btn()

@then('enter recipient and message body')
def step_impl(context):
	context.current_page = MessagingPageObject()
	context.current_page.msg_details()
	
