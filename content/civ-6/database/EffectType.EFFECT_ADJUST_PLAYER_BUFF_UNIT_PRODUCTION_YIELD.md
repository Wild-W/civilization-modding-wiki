---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_BUFF_UNIT_PRODUCTION_YIELD
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_BUFF_UNIT_PRODUCTION_YIELD
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="WC_RES_UNIT_PRODUCTION_YIELD_DEBUFF"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"WC_RES_UNIT_PRODUCTION_YIELD_DEBUFF",
		"MODIFIER_PLAYERS_ADJUST_UNIT_BUFF_PRODUCTION_YIELD"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"WC_RES_UNIT_PRODUCTION_YIELD_DEBUFF",
		"Amount",
		"-100"
	);
	
```

