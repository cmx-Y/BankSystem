<template>
  <div>
    <Form ref="formValidate" :model="formValidate" :rules="ruleValidate" :label-width="200" label-position="right">
      <Row>
        <Col span = "7"></Col>
        <Col span="7">
          <FormItem label="Idnum"  prop="idnum">
            <Input v-model="formValidate.idnum" placeholder="Enter your identity number" style="width: 300px"></Input>
          </FormItem>
        </Col>
      </Row>

      <Row>
        <Col span = "7"></Col>
        <Col span="7">
          <FormItem label="Name"  prop="name">
            <Input v-model="formValidate.name" placeholder="Enter your name" style="width: 300px"></Input>
          </FormItem>
        </Col>
      </Row>

      <Row>
        <Col span = "7"></Col>
        <Col span="7">
          <FormItem label="Tel" prop="tel">
            <Input v-model="formValidate.tel" placeholder="Enter your telegram" style="width: 300px"></Input>
          </FormItem>
        </Col>
      </Row>

      <Row>
        <Col span = "7"></Col>
        <Col span="7">
          <FormItem label="Addr" prop="addr">
            <Input v-model="formValidate.addr" placeholder="Enter your address" style="width: 300px"></Input>
          </FormItem>
        </Col>
      </Row>

      <Row>
        <Col span = "7"></Col>
        <Col span="7">
          <FormItem label="Password1" prop="pswd1">
            <Input v-model="formValidate.pswd1" placeholder="Enter your password" style="width: 300px"></Input>
          </FormItem>
        </Col>
      </Row>

      <Row>
        <Col span = "7"></Col>
        <Col span="7">
          <FormItem label="Password2" prop="pswd2">
            <Input v-model="formValidate.pswd2" placeholder="Enter your password again" style="width: 300px"></Input>
          </FormItem>
        </Col>
      </Row>

      <Row>
        <Col span = "7"></Col>
        <Col span="7">
          <FormItem label="Contact" prop="contact">
            <Input v-model="formValidate.contact" placeholder="Enter your contact name" style="width: 300px"></Input>
          </FormItem>
        </Col>
      </Row>

      <Row>
        <Col span = "7"></Col>
        <Col span="7">
          <FormItem label="ContactTel" prop="contact_tel">
            <Input v-model="formValidate.contact_tel" placeholder="Enter your contact tel" style="width: 300px"></Input>
          </FormItem>
        </Col>
      </Row>

      <Row>
        <Col span = "7"></Col>
        <Col span="7">
          <FormItem label="ContactEmail" prop="contact_email">
            <Input v-model="formValidate.contact_email" placeholder="Enter your contact email" style="width: 300px"></Input>
          </FormItem>
        </Col>
      </Row>

      <Row>
        <Col span = "7"></Col>
        <Col span="7">
          <FormItem label="ContactRelationship" prop="relation">
            <Input v-model="formValidate.relation" placeholder="Enter your relationship with contact" style="width: 300px"></Input>
          </FormItem>
        </Col>
      </Row>

      <FormItem>
          <Button type="primary" @click="Submit()">Submit</Button>
      </FormItem>

    </Form>
  </div>
</template>

<script>
import {postSignup} from '../api/api.js'
import {signinSuccess} from '../api/jumpApi.js'


export default {
  name: 'ClientSignUp',
  data () {
      return {
          formValidate: {
              idnum: '',
              name: '',
              tel: '',
              addr: '',
              pswd1: '',
              pswd2: '',
              contact: '',
              contact_tel: '',
              contact_email: '',
              relation: ''
          },
          ruleValidate: {
              name: [
                  { required: true, message: 'The name cannot be empty', trigger: 'blur' }
              ]
          }
      }
    },
    methods: {
        Submit(){
          let idata = this.formValidate
          postSignup(idata)
        },
        handleSubmit (name) {
            this.$refs[name].validate((valid) => {
                if (valid) {
                    this.$Message.success('Success!');
                } else {
                    this.$Message.error('Fail!');
                }
            })
        },
        handleReset (name) {
            this.$refs[name].resetFields();
        }
    }
}
</script>

