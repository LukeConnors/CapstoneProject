import { useDispatch, useSelector } from "react-redux";
import { useModal } from "../../context/Modal";
import React, { useEffect, useState } from "react";
import { io } from "socket.io-client";
import { getUserMessages } from "../../store/messages";
import "./ChatModal.css"
let socket;


function ChatModal({ recipientId, name }) {
    const dispatch = useDispatch();
    const { closeModal } = useModal();
    const messages = useSelector(state => state.messages)
    const messageIds = Object.keys(messages || {})
    const [messageInput, setMessageInput] = useState('')
    const user = useSelector(state => state.session.user)
    console.log("THIS IS THE RECIPIENT", recipientId)

    useEffect(() => {
        dispatch(getUserMessages(recipientId))
    }, [dispatch])

    useEffect(() => {
        socket = io()

        socket.on('message', () => {
            dispatch(getUserMessages(recipientId))
        })
        return (() => {
            socket.disconnect()
        })


    })

    const updateMessageInput = (e) => {
        setMessageInput(e.target.value)
    };

    const sendMessage = (e) => {
        e.preventDefault()
        socket.emit("message", { message: messageInput }, recipientId)
        dispatch(getUserMessages(recipientId))
        setMessageInput('')
    }


    return (
        <div className="chat-container">
            <h1>Chatting with {name}</h1>
            <div className="messages-container">
                {messageIds.map((messageId) => {
                    const message = messages[messageId]
                    return message.sender_id === user.id ? (
                        <>
                        <div className="my-message">
                            <p>{message.message}</p>
                        </div>
                        </>
                    ) : (
                        <div className="their-message">
                            <p>{message.message}</p>
                        </div>
                    )
                })}
            </div>
            <form onSubmit={sendMessage}>
                <input
                    value={messageInput}
                onChange={updateMessageInput}
                >
                </input>
                <button type="submit">Send</button>
            </form>
        </div>

    )

}

export default ChatModal;
