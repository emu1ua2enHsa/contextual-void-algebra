library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity IPC_ALU_8BIT is
    Port (
        clk            : in STD_LOGIC;
        reset          : in STD_LOGIC;
        operand_A      : in STD_LOGIC_VECTOR(7 downto 0);
        operand_B      : in STD_LOGIC_VECTOR(7 downto 0);
        op_code        : in STD_LOGIC_VECTOR(1 downto 0);
        active_out     : out STD_LOGIC_VECTOR(7 downto 0);
        vacancy_out    : out STD_LOGIC_VECTOR(7 downto 0);
        evac_trigger   : out STD_LOGIC
    );
end IPC_ALU_8BIT;

architecture Behavioral of IPC_ALU_8BIT is
    signal reg_active  : unsigned(7 downto 0) := (others => '0');
    signal reg_vacancy : unsigned(7 downto 0) := (others => '0');
    signal sig_trigger : STD_LOGIC := '0';
begin
    process(clk, reset)
    begin
        if reset = '1' then
            reg_active  <= (others => '0');
            reg_vacancy <= (others => '0');
            sig_trigger <= '0';
        elsif rising_edge(clk) then
            sig_trigger <= '0'; 
            case op_code is
                when "10" =>
                    if operand_A = operand_B then
                        reg_active  <= (others => '0');
                        reg_vacancy <= unsigned(operand_A);
                        sig_trigger <= '1';
                    elsif unsigned(operand_A) < unsigned(operand_B) then
                        reg_active  <= (others => '0');
                        reg_vacancy <= unsigned(operand_B) - unsigned(operand_A);
                        sig_trigger <= '1';
                    else
                        reg_active  <= unsigned(operand_A) - unsigned(operand_B);
                        reg_vacancy <= (others => '0');
                        sig_trigger <= '0';
                    endif;
                when others =>
                    reg_active  <= unsigned(operand_A);
                    reg_vacancy <= (others => '0');
                    sig_trigger <= '0';
            end case;
        end if;
    end process;
    active_out   <= std_logic_vector(reg_active);
    vacancy_out  <= std_logic_vector(reg_vacancy);
    evac_trigger <= sig_trigger;
end Behavioral;

