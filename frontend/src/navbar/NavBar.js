import React, { useContext } from 'react';
import { Link, NavLink } from "react-router-dom";
import UserContext from "../auth/UserContext";
import "./NavBar.css";

// When user is logged in, shows links to main areas of site. When not,
// shows link to Login and Signup forms
function NavBar({ logout }) {

const { currentUser } = useContext(UserContext);
console.debug("NavBar", "currentUser=", currentUser);

// Logger in user
function loggedInNav() {
    return (
        <ul className="navbar-nav ml-auto">
            <li className="nav-item mr-4">
                <NavLink exact path="/player/stats">
                    Player Stats
                </NavLink>
            </li>

            <li className="nav-item mr-4">
                <NavLink className="nav-link" to="/avg">
                    Average Joe Stats
                </NavLink>
            </li>

            <li className="nav-item mr-4">
                <NavLink className="nav-link" to="/profile">
                    
                </NavLink>
            </li>

            <li className="nav-item">
            <Link className="nav-link" to="/" onClick={logout}>
              Log out {currentUser.first_name || currentUser.username}
            </Link>
          </li>

        </ul>
    );
}

function loggedOutNav() {
    return (
        <ul className="navbar-nav ml-auto">
          <li className="nav-item mr-4">
            <NavLink className="nav-link" to="/login">
              Login
            </NavLink>
          </li>
          <li className="nav-item mr-4">
            <NavLink className="nav-link" to="/signup">
              Sign Up
            </NavLink>
          </li>
        </ul>
    );
  }

  return (

    <nav className="Navigation navbar navbar-expand-md">
      <Link className="navbar-brand" to="/">
        OverPaid
      </Link>
      {currentUser ? loggedInNav() : loggedOutNav()}
    </nav>
);
}
 


export default NavBar;