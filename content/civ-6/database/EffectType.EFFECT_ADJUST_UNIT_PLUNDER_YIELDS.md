---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_PLUNDER_YIELDS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_PLUNDER_YIELDS
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="RAJENDRA_CHOLA_PLUNDER_BONUS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"RAJENDRA_CHOLA_PLUNDER_BONUS",
		"MODIFIER_PLAYER_UNIT_ADJUST_PLUNDER_YIELDS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"RAJENDRA_CHOLA_PLUNDER_BONUS",
		"Amount",
		40
	);
	
```

