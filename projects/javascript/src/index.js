///////////////////////
// Welcome to Cursor //
///////////////////////

/*
Step 1: Try generating a react component that lets you play tictactoe with Cmd+K or Ctrl+K on a new line.
  - Then integrate it into the code below and run with npm start

Step 2: Try highlighting all the code with your mouse, then hit Cmd+k or Ctrl+K. 
  - Instruct it to change the game in some way (e.g. add inline styles, add a start screen, make it 4x4 instead of 3x3)

Step 3: Hit Cmd+L or Ctrl+L and ask the chat what the code does

Step 4: To try out cursor on your own projects, go to the file menu (top left) and open a folder.
*/

import React from 'react';
import ReactDOM from 'react-dom/client';

function StartScreen({ onStart }) {
  return (
    <div style={{ textAlign: 'center', marginTop: '80px' }}>
      <h1>틱택토 게임 (4x4)</h1>
      <p>두 명이 번갈아가며 X와 O를 놓고, 가로/세로/대각선으로 4개를 먼저 맞추면 승리합니다.</p>
      <button 
        style={{ fontSize: '20px', padding: '10px 30px', cursor: 'pointer' }}
        onClick={onStart}
      >
        게임 시작
      </button>
    </div>
  );
}

function TicTacToe() {
  const size = 4;
  const [board, setBoard] = React.useState(Array(size * size).fill(null));
  const [isXNext, setIsXNext] = React.useState(true);

  const calculateWinner = (squares) => {
    // 가로
    for (let row = 0; row < size; row++) {
      let start = row * size;
      if (
        squares[start] &&
        squares[start] === squares[start + 1] &&
        squares[start] === squares[start + 2] &&
        squares[start] === squares[start + 3]
      ) {
        return squares[start];
      }
    }
    // 세로
    for (let col = 0; col < size; col++) {
      if (
        squares[col] &&
        squares[col] === squares[col + size] &&
        squares[col] === squares[col + size * 2] &&
        squares[col] === squares[col + size * 3]
      ) {
        return squares[col];
      }
    }
    // 대각선 (좌상-우하)
    if (
      squares[0] &&
      squares[0] === squares[5] &&
      squares[0] === squares[10] &&
      squares[0] === squares[15]
    ) {
      return squares[0];
    }
    // 대각선 (우상-좌하)
    if (
      squares[3] &&
      squares[3] === squares[6] &&
      squares[3] === squares[9] &&
      squares[3] === squares[12]
    ) {
      return squares[3];
    }
    return null;
  };

  const handleClick = (i) => {
    if (calculateWinner(board) || board[i]) {
      return;
    }
    const nextBoard = board.slice();
    nextBoard[i] = isXNext ? 'X' : 'O';
    setBoard(nextBoard);
    setIsXNext(!isXNext);
  };

  const winner = calculateWinner(board);
  const status = winner
    ? `승자: ${winner}`
    : board.every(square => square)
    ? '무승부!'
    : `다음 플레이어: ${isXNext ? 'X' : 'O'}`;

  const renderSquare = (i) => {
    return (
      <button
        className="square"
        onClick={() => handleClick(i)}
        style={{
          width: '50px',
          height: '50px',
          margin: '2px',
          fontSize: '22px',
          fontWeight: 'bold',
          backgroundColor: '#fff',
          border: '1px solid #999',
          cursor: 'pointer'
        }}
      >
        {board[i]}
      </button>
    );
  };

  // 4x4 보드 렌더링
  const boardRows = [];
  for (let row = 0; row < size; row++) {
    const rowSquares = [];
    for (let col = 0; col < size; col++) {
      rowSquares.push(renderSquare(row * size + col));
    }
    boardRows.push(
      <div key={row} style={{ display: 'flex' }}>
        {rowSquares}
      </div>
    );
  }

  return (
    <div style={{ textAlign: 'center', marginTop: '20px' }}>
      <div style={{ marginBottom: '20px', fontSize: '20px' }}>{status}</div>
      <div style={{ display: 'inline-block' }}>{boardRows}</div>
    </div>
  );
}

function App() {
  const [started, setStarted] = React.useState(false);
  return started ? <TicTacToe /> : <StartScreen onStart={() => setStarted(true)} />;
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
