import React from 'react'
import { Nav, NavbarContainer, NavLogo } from './NavbarElements'


const Navbar  = () => {
    return (
        <>
            <Nav>
                <NavbarContainer>
                    <NavLogo to='/'>The Tanko Records</NavLogo>
                    <NavMenu>
                        <NavLink to="/baba-and-mama" active Style>
                            Tanko and Maryamu
                        </NavLink>
                        <NavLink to="/children" activeStyle>
                            Children
                        </NavLink>
                        <NavLink to="/grand-children" activeStyle>
                            Grand Children
                        </NavLink>
                        <NavLink to="/great-grand-children" activeStyle>
                            Great Grand Children
                        </NavLink>
                    </NavMenu>
                    <NavBtn>
                        <NavBtnLink to='/signout'>Sign Out</NavBtnLink>
                    </NavBtn>
                    <div className="search-box">
                        <input
                        type="text"
                        className="search-bar"
                        placeholder="Search Names..."
                        />
                    </div>
                </NavbarContainer>
            </Nav>
        </>
    );
};

export default Navbar;
