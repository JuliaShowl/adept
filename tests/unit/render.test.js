import { getByText, render , screen, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom';
import User from '../../frontend/src/User';
import Statistics from '../../frontend/src/Stats';
import Docs from '../../frontend/src/Docs';

test('render user component', async () => {
    const mockResponse = { data: { name: 'John Doe', email: 'john@example.com', role: 'Admin' } };
    render(<User users={mockResponse}/>)
    const userElement = screen.getByTestId('user-component')
    expect(userElement).toBeInTheDocument()
    const dropdownElement = screen.getAllByTestId('dropdown-content')
    waitFor(() => expect(dropdownElement).not.toBeVisible())
});

test('render stats component', async () => {
    const mockResponse = { data: { complete: 4, inREview: 2, inDraft: 3, pendingApproval: 2, totalDocuments: 13 } };
    render(<Statistics stats={mockResponse}/>)
    const statsElement = screen.getByTestId('stats-component')
    expect(statsElement).toBeInTheDocument()
});