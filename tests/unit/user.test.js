import { render , screen } from '@testing-library/react'
import User from '../../frontend/src/User';


test('render user component', async () => {
    const mockResponse = { data: { name: 'John Doe', email: 'john@example.com', role: 'Admin' } };
    render(<User users={mockResponse}/>)
})