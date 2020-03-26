import React, {Component} from 'react'

import ReactDOM from 'react-dom';
import FacebookLogin from 'react-facebook-login';
import {Link} from 'react-router-dom'

export default class Facebook extends Component{
    
   state={
       isLoggedIn: false,
       userID:'',
       name:'',
       email:'',
       picture:'',
       facebooktoken:''
       
   }
   
   responseFacebook = response =>{
       console.log(response);
       
       this.setState({
           isLoggedIn : true,
           userID : response.userID,
           name : response.name,
           email : response.email,
           picture : response.picture.data.url,
           facebooktoken :response.accessToken
       });
   }
  

    componentClicked = () => console.log("clicked");
    
    render(){
        
        var fbContent;
        if(this.state.isLoggedIn){
            
            window.location="./MainLayout";
            localStorage.setItem("fullname",this.state.name);
            localStorage.setItem("userimg",this.state.picture);
            localStorage.setItem("facebookid",this.state.userID);
            localStorage.setItem("fbtoken",this.state.facebooktoken);
            
        }
        else{
        
    fbContent = (   <FacebookLogin
    appId="206217843919244"
    autoLoad={true}
    fields="name,email,picture"
    onClick={this.componentClicked}
    callback={this.responseFacebook} />
            
                )
            
        }
                       
        return <div className="my-facebook-button-class"> {fbContent} </div>;
        
        
        
        
    }
    
    
    
    
}