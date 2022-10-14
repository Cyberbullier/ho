import React, { useState } from 'react';
import axios from "axios";
import styled from 'styled-components';

const Button = styled.button`
  background-color: black;
  color: white;
  font-size: 20px;
  padding: 10px 60px;
  border-radius: 5px;
  margin: 10px 0px;
  cursor: pointer;
  &:disabled {
    color: grey;
    opacity: 0.7;
    cursor: default;
  }
`;
const ButtonToggle = styled(Button)`
  opacity: 0.6;
  ${({ active }) =>
    active &&
    `
    opacity: 1;
  `}
`;
const ButtonGroup = styled.div`
  display: flex;
`;

const Mushroom_tips = ['Enoki','King Oyster'];
function App() {

//endpoint use effects
const [add_enoki_cart, setAddEnokiCart] = useState(null)
const [remove_enoki_cart, setRemoveEnokiCart] = useState(null)
const [add_oyster_cart, setAddOysterCart] = useState(null)
const [remove_Oyster_cart, setRemoveOysterCart] = useState(null)

const [active, setActive] = useState(Mushroom_tips[0]);

function get_enoki_from_stock() {
  axios({
    method: "GET",
    url:"/add-enoki",
  })
  .then((response) => {
    const res =response.data
    setAddEnokiCart(({
      price: res.price,
      count: res.count}))
  }).catch((error) => {
    if (error.response) {
      console.log(error.response)
      console.log(error.response.status)
      console.log(error.response.headers)
      }
  })}





  function add_mushroom(){
    return (
      <ButtonGroup>
        {Mushroom_tips.map(type => (
          <ButtonToggle
            key={type}
            active={active === type}
            onClick={() => setActive(type)}
          >
            {type}
          </ButtonToggle>
        ))}
      </ButtonGroup>
    );
  };


  function remove_mushroom(){
    return (
      <ButtonGroup>
        {Mushroom_tips.map(type => (
          <ButtonToggle
            key={type}
            active={active === type}
            onClick={() => setActive(type)}
          >
            {type}
          </ButtonToggle>
        ))}
      </ButtonGroup>
    );
  };
};


export default App;

