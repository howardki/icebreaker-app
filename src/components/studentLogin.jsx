import React, { Component } from 'react'
import '../index.css'
import '../App.css'
import './signin.css'
// import 'bootstrap/dist/css/bootstrap.css'


class StudentLogin extends Component {
  state = {}
  render() {
    return (
      <div className="wrapper">
        <div className="header">
          <div className="logo">
            <h1> Icebreaker </h1>
          </div>
        </div>
      <div className="student" >
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous"/>
      <body className="text-center">
        <form className="form-signin">
          <h1 className="h4 mb-3 font-weight-normal">Student Login</h1>
          <label for="fullName" className="sr-only">Full Name</label>
          <input type="name" id="fullName" className="form-control" placeholder="Full Name" required autofocus/>
          <label for="inputPassword" className="sr-only">Key Word</label>
          <input type="password" id="inputPassword" className="form-control" placeholder="Key Word" required/>
          <div className="checkbox mb-3">
          </div>
          <button className="btn btn-lg btn-primary btn-block" type="submit">Enter Classroom </button>
          <p className="mt-5 mb-3 text-muted">&copy; 2017-2018</p>
        </form>
      </body>
      </div>

      <div className="instructor" >
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous"/>
      <body className="text-center">
        <form className="form-signin">
          <h1 className="h4 mb-3 font-weight-normal">Instructor Login</h1>
          <label for="fullName" className="sr-only">Full Name</label>
          <input type="name" id="fullName" className="form-control" placeholder="Full Name" required autofocus/>
          <label for="inputPassword" className="sr-only">Classroom Key</label>
          <input type="password" id="inputPassword" className="form-control" placeholder="Classroom Key" required/>
          <div className="checkbox mb-3">
          </div>
          <button className="btn btn-lg btn-primary btn-block" type="submit">Create Classroom </button>
          <p className="mt-5 mb-3 text-muted">&copy; 2017-2018</p>
        </form>
      </body>
      </div>
      </div>
    )
  }
}

export default StudentLogin;
