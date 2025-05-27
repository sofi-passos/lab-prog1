MOD = 10**9 + 7

def countRecognizedStrings(R, L):
    from collections import defaultdict

    class State:
        def __init__(self):
            self.transitions = defaultdict(list)
            self.epsilon = []

    def parse_expr(expr):
        idx = [0]

        def parse():
            start = State()
            end = State()
            if expr[idx[0]] in 'ab':
                ch = expr[idx[0]]
                idx[0] += 1
                start.transitions[ch].append(end)
            elif expr[idx[0]] == '(':
                idx[0] += 1
                left = parse()
                if expr[idx[0]] == '|':
                    idx[0] += 1
                    right = parse()
                    idx[0] += 1
                    start.epsilon.extend([left[0], right[0]])
                    left[1].epsilon.append(end)
                    right[1].epsilon.append(end)
                elif expr[idx[0]] == ')':
                    idx[0] += 1
                    start.epsilon.append(left[0])
                    left[1].epsilon.append(end)
                elif expr[idx[0]] == '*':
                    idx[0] += 2
                    start.epsilon.extend([left[0], end])
                    left[1].epsilon.extend([left[0], end])
                else:
                    right = parse()
                    idx[0] += 1
                    start.epsilon.append(left[0])
                    left[1].epsilon.append(right[0])
                    right[1].epsilon.append(end)
            return (start, end)

        return parse()

    def epsilon_closure(states):
        stack = list(states)
        closure = set(states)
        while stack:
            state = stack.pop()
            for next_state in state.epsilon:
                if next_state not in closure:
                    closure.add(next_state)
                    stack.append(next_state)
        return closure

    def nfa_to_dfa(start, end):
        state_map = {}
        dfa_start = frozenset(epsilon_closure([start]))
        queue = [dfa_start]
        state_map[dfa_start] = 0
        transitions = {}
        final_states = set()
        idx = 1
        while queue:
            curr = queue.pop()
            transitions[state_map[curr]] = {}
            if end in curr:
                final_states.add(state_map[curr])
            for ch in 'ab':
                next_states = set()
                for st in curr:
                    for nxt in st.transitions.get(ch, []):
                        next_states.update(epsilon_closure([nxt]))
                next_states = frozenset(next_states)
                if next_states and next_states not in state_map:
                    state_map[next_states] = idx
                    queue.append(next_states)
                    idx += 1
                if next_states:
                    transitions[state_map[curr]][ch] = state_map[next_states]
        return transitions, 0, final_states

    start, end = parse_expr(R)
    transitions, start_id, final_states = nfa_to_dfa(start, end)
    states = list(transitions.keys())
    dp = [0] * len(states)
    dp[start_id] = 1

    for _ in range(L):
        next_dp = [0] * len(states)
        for s in states:
            for ch in 'ab':
                if ch in transitions[s]:
                    ns = transitions[s][ch]
                    next_dp[ns] = (next_dp[ns] + dp[s]) % MOD
        dp = next_dp

    return sum(dp[s] for s in final_states) % MOD
