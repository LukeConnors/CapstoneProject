
import { useDispatch, useSelector } from "react-redux";
import { useModal } from "../../context/Modal";
import React, { useEffect, useState, useRef } from "react";
import { io } from "socket.io-client";
import { getUserMessages } from "../../store/messages";
import "./ChatModal.css";
let socket;

function ChatModal({ recipientId, name }) {
  const dispatch = useDispatch();
  const { closeModal } = useModal();
  const messages = useSelector((state) => state.messages);
  const messageIds = Object.keys(messages || {});
  const [messageInput, setMessageInput] = useState("");
  const user = useSelector((state) => state.session.user);
  const messagesContainerRef = useRef(null);
  const scrollRef = useRef(null); // New ref for scrolling

  const scrollToBottom = () => {
    if (scrollRef.current) {
      scrollRef.current.scrollIntoView({ behavior: "smooth" });
    }
  };

  useEffect(() => {
    dispatch(getUserMessages(recipientId));
  }, [dispatch, recipientId]);

  useEffect(() => {
    socket = io();

    socket.on("connect", () => {
      console.log("Socket connected");
    });

    socket.on("message", (data) => {
      dispatch(getUserMessages(recipientId));
      scrollToBottom();
    });

    socket.on("disconnect", () => {
      console.log("Socket disconnected");
    });

    socket.on("error", (error) => {
      console.error("Socket error:", error);
    });

    return () => {
      socket.disconnect();
    };
  }, [recipientId]);

  const updateMessageInput = (e) => {
    setMessageInput(e.target.value);
  };

  const sendMessage = async (e) => {
    e.preventDefault();
    await socket.emit("message", { message: messageInput }, recipientId);
    await dispatch(getUserMessages(recipientId));
    setMessageInput("");
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  return (
    <div className="chat-container">
      <h1>Chatting with {name}</h1>
      <div className="messages-container">
        {messageIds.map((messageId) => {
          const message = messages[messageId];
          return message.sender_id === user.id ? (
            <div className="my-message" key={messageId}>
              <p>{message.message}</p>
            </div>
          ) : (
            <div className="their-message" key={messageId}>
              <p>{message.message}</p>
            </div>
          );
        })}
        <div ref={scrollRef}></div>
      </div>
      <form className="mess-form" onSubmit={sendMessage}>
        <input className="mess-input" value={messageInput} onChange={updateMessageInput}></input>
        <button className="mess-button" type="submit">Send</button>
      </form>
      <div className="close-button-div">
      <button className="close-button" onClick={closeModal}>Close Chat</button>
      </div>
    </div>
  );
}

export default ChatModal;
