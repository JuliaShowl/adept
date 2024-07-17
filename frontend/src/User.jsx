import React from 'react'

const User = ({users}) => {
    return <div>
        <div className='dropdown'>
            {users.name}
            <div className='dropdown-content'>
                {users.email}<br />
                {users.role}
            </div>
        </div>
    </div>
}

export default User