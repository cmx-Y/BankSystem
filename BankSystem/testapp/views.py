from django.shortcuts import render
from django.db import connection
from testapp.models import Subbank
from rest_framework.response import Response
from django.http import JsonResponse
import json
# Create your views here.

from rest_framework import viewsets
from testapp.serializer import SubbankSerializer


from django.http import HttpResponse

POST_FORM = '''
<form method='post' action='/testapp/'>
    user:<input type='text' name='uname'>
    <input type='submit' value='sss'>
</form>
'''

HTM = '''
<form action='/testapp/' method='post'> 
        First name:<br> 
        <input type='text' name='firstname'> 
        <br> 
        Last name:<br> 
        <input type='text' name='lastname'> 
        <div class='button'> 
        <button type='submit' > tijiao </button>
        </div> 
        </form>
<a href="jump/"> register </a>
'''

def testfunc(request):
    if request.method == 'GET':
        return HttpResponse(HTM)
    else:
        print(request.POST)
        print(request.POST.get('firstname'))
        return HttpResponse("ok")

class BankViewSet(viewsets.ModelViewSet):
    queryset = Subbank.objects.all()
    serializer_class = SubbankSerializer

def jumpfunc(request):
    return HttpResponse("jump ok!!")

def restest(request):
    if request.method == 'POST':
        mydi = json.loads(request.body)
        print(mydi)
        print(mydi['user'])
        print(mydi['password'])
        return JsonResponse('', safe=False)
    else:
        queryset = Subbank.objects.all()
        serializer_class = SubbankSerializer(queryset, many=True)
        return JsonResponse(serializer_class.data, safe=False)



## insert into table
#  b = Subbank(bankname='XMSub', city='XiaMen', asset=66666666.66)
#  b.save()

## select from table
#  sp_entry = Subbank.objects.filter(city='XiaMen')
#  for e in sp_entry:
#      print(e.bankname)


#        {bankname: 'testbank1', city: 'testcity1', asset: 0},
#        {bankname: 'testbank2', city: 'testcity2', asset: 0},


'''
<template>
    <div>
      <Form ref="formInline" :model="formInline" :rules="ruleInline" inline>
        <FormItem prop="user">
            <Input type="text" v-model="formInline.user" placeholder="Identity">
                <Icon type="ios-person-outline" slot="prepend"></Icon>
            </Input>
        </FormItem>
        <br>
        <FormItem prop="password">
            <Input type="password" v-model="formInline.password" placeholder="Password">
                <Icon type="ios-lock-outline" slot="prepend"></Icon>
            </Input>
        </FormItem>
        <br>
        <FormItem>
            <Button type="primary" @click="Submit()">Signin</Button>
        </FormItem>

      </Form>

      <ul>
        <li v-for="(bank,idx) in banks" :key="idx">
          {{bank.bankname}}-{{bank.city}}-{{bank.asset}}
        </li>
      </ul>

    </div>
</template>

<script>
import {getBanks, postSignin, postTest} from '../api/api.js'


export default {
  name: 'HomePage',

  data () {
    return {
      formInline: {
                    user: '',
                    password: ''
                },
      ruleInline: {
          user: [
              { required: true, message: 'Please fill in the Identity', trigger: 'blur' }
          ],
          password: [
              { required: true, message: 'Please fill in the Password.', trigger: 'blur' },
          ]
      },

      banks: [ ],

      inputBank: {
        "name": "",
        "author": "",
      }
    }
  },

  methods: {
    Submit(){
      let idata = {
        user: this.formInline.user,
        password: this.formInline.password
      }
      postTest(idata)
    },

    loadBanks () {
      getBanks().then(response => {
        this.banks = response.data
        console.log(response.data)
      })
    }
  },

  created: function () {
    this.loadBanks()
  }
}
</script>
'''