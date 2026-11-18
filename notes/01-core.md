# Compute an accidental-corruption checksum: implementation

## What the example does

CRC32 detects many transmission errors but is not cryptographically secure. Format as eight hex digits to keep a stable representation.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
"hello"
```

Expected result:

```json
"3610a686"
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
