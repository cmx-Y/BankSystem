import axiosInstance from './index'

const axios = axiosInstance

axios.defaults.baseURL='http://127.0.0.1:8000/'

export const getBanks = () => {return axios.get('testapp/restest')}
export const postSignin = (idata) => {return axios({
    url: 'bank/client/signin/',
    method: 'post',
    data: idata,
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  })}

export const postSignup = (idata) => {return axios({
    url: 'bank/client/signup/',
    method: 'post',
    data: idata,
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
})}