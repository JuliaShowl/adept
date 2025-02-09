import React from 'react'

const User = ({users}) => {
    return <div data-testid='user-component'>
        <div className='dropdown'>
            Welcome&nbsp;
            <span className='name'>
                {users.name}
            </span>
            <span className='down-caret'>&#9660;</span>
            <span className='up-caret'>&#9650;</span>
            <span></span>
            <div className='dropdown-content' data-testid='dropdown-content'>
                {users.email}<br />
                {users.role}
            </div>
        </div>
    </div>
}

export default User