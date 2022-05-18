import axiosInstance from './index'

const axios = axiosInstance

export const signinSuccess = () => {return axios({
    url: 'http://127.0.0.1:8080/#/ClientPage',
    method: 'get',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  })}

