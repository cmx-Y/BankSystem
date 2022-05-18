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
        <Button type="primary" @click="Signup()">Signup</Button>
        </FormItem>
        
        <FormItem>
            <Button type="primary" @click="Submit()">Signin</Button>
        </FormItem>

      </Form>

      <br>
      
    </div>
</template>

<script>
import {postSignin} from '../api/api.js'
import {signinSuccess} from '../api/jumpApi.js'


export default {
  name: 'ClientSignin',

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
    }
  },

  methods: {
    Submit(){
      let idata = {
        user: this.formInline.user,
        password: this.formInline.password
      }
      postSignin(idata).then(response => {
        if(response.data.found == false){
          this.$Message.info('User doesn\'t exist!')
        }
        else if(response.data.pwd_right == false){
          this.$Message.info('Id or password wrong!')
        }
        else{
          this.$Message.info('Sign in success!')
          this.$router.push({path:'/ClientPage'})
        }
      })
    },
    Signup(){
      this.$router.push({path:'/ClientSignUp'})
    }
  },

  
}
</script>

