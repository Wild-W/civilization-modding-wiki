---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_BAN_CHOP
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_BAN_CHOP
>
> * Class: `PLAYERS`
> * Parameters:
>	* NoRemove `Boolean`

## Samples
```SQL {title="WC_RES_DEFORESTATION_BAN"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"WC_RES_DEFORESTATION_BAN",
		"MODIFIER_PLAYERS_ADJUST_CHOP_BAN"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"WC_RES_DEFORESTATION_BAN",
		"NoRemove",
		1
	);
	
```

