class Solution {
    public int maxNumberOfBalloons(String text) {
        Map<Character, Integer> characters = new HashMap<>();

        for (int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);
            characters.put(c, characters.getOrDefault(c, 0) + 1);
        }

        int[] balloonChars = {
            characters.getOrDefault('b', 0) / 1,
            characters.getOrDefault('a', 0) / 1,
            characters.getOrDefault('l', 0) / 2,
            characters.getOrDefault('o', 0) / 2,
            characters.getOrDefault('n', 0) / 1,
        };
        
        int balloons = Arrays.stream(balloonChars)
                        .min()
                        .getAsInt();
        return balloons;
    }

}