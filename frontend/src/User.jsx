import React from 'react'

const User = ({users}) => {
    return <div>
        <h2>Welcome</h2>
        {users.name}
    </div>
}

export default User