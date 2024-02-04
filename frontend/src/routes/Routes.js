import React from "react";
import { Routes as Route, NavLink, Navigate  } from "react-router-dom";

import LoginForm from "../auth/LoginForm";
import SignupForm from "../auth/SignupForm";
import Homepage from "../homepage/Homepage";
import ProfileForm from "../profile/ProfileForm";

import AllAvgStats from "../avg/AllAvgStats";
import AvgStatsByPosition from "../avg/AvgStatsByPosition";

import AllPlayerStats from "../player/AllPlayerStats";
import PlayerStatsByName from "../player/PlayerStatsByName";




function Routes({ login, signup }) {
      
    return (
        <div className="pt-5">
            <Routes>

                <li className="nav-item mr-4">
                <Route path="/">
                    <Homepage />
                </Route>
                </li>

                <li className="nav-item mr-4">
                <Route exact path="/login">
                    <LoginForm login={login}/>
                </Route>
                </li>

                <li className="nav-item mr-4">
                <Route exact path="/signup">
                    <SignupForm signup={signup}/>
                </Route>
                </li>

                <li className="nav-item mr-4">
                <Route path="/profile">
                    <ProfileForm />
                </Route>
                </li>

                <li className="nav-item mr-4">
                    <NavLink exact path="/player/stats" >
                        <AllPlayerStats />
                    </NavLink>
                </li>

                <li className="nav-item mr-4">
                <Route exact path="/player/stats/:name">
                    <PlayerStatsByName />
                </Route>
                </li>
            
                <li className="nav-item mr-4">
                <Route exact path="/avg/:position">
                    <AvgStatsByPosition />
                </Route>
                </li>

                <li className="nav-item mr-4">
                    <Route exact path="/avg">
                    <AllAvgStats />
                    </Route>
                </li>

            
                <Navigate to="/" />

            </Routes>
        </div>
    )
}

export default Routes;