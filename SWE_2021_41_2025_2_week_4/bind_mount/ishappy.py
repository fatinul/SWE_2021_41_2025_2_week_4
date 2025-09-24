def isHappy(n):
  seen=set()
  while n != 1 and n not in seen:
      seen.add(n)
      n = sum(int(digits)**2 for digits in str(n))
  if n != 1:
    return False
  elif n == 1:
    return True

if __name__ == "__main__":
    sample0_output = isHappy(19)
    sample1_output = isHappy(2)

    with open("/app/bind_mount/output.txt", "w") as f:
        f.write(f"19: {sample0_output}\n")
        f.write(f"2: {sample1_output}\n")

    print("Results saved to /app/bind_mount/output.txt")