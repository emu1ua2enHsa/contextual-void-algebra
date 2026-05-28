library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity ipc_alu_tb is
end ipc_alu_tb;

architecture Simulation of ipc_alu_tb is
    signal clk         : STD_LOGIC := '0';
    signal rst         : STD_LOGIC := '0';
    signal operand_a   : STD_LOGIC_VECTOR(7 downto 0) := (others => '0');
    signal operand_b   : STD_LOGIC_VECTOR(7 downto 0) := (others => '0');
    signal opcode      : STD_LOGIC_VECTOR(1 downto 0) := (others => '0');
    signal result      : STD_LOGIC_VECTOR(7 downto 0);
    signal vacuum_flag : STD_LOGIC;
    signal tier_out    : STD_LOGIC_VECTOR(7 downto 0);

    constant clk_period : time := 10 ns;
begin
    uut: entity work.ipc_alu
        port map (
            clk => clk, rst => rst, operand_a => operand_a, operand_b => operand_b,
            opcode => opcode, result => result, vacuum_flag => vacuum_flag, tier_out => tier_out
        );

    clk_process : process
    begin
        clk <= '0'; wait for clk_period/2;
        clk <= '1'; wait for clk_period/2;
    end process;

    stim_proc: process
    begin
        rst <= '1'; wait for 20 ns;
        rst <= '0'; wait for 10 ns;

        -- Test Case 1: Standard Addition
        operand_a <= x"05"; operand_b <= x"03"; opcode <= "00"; wait for clk_period;
        
        -- Test Case 2: Standard Subtraction (Unequal)
        operand_a <= x"0A"; operand_b <= x"04"; opcode <= "01"; wait for clk_period;

        -- Test Case 3: IPC Reversible Subtraction (Equal Values)
        operand_a <= x"FF"; operand_b <= x"FF"; opcode <= "01"; wait for clk_period;

        wait;
    end process;
end Simulation;

