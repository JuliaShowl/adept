import { render , screen } from '@testing-library/react'
import App from '../../frontend/src/App'

/**
 * @jest-environment jsdom
 */

test('render page', () => {
    render(<App/>);
})