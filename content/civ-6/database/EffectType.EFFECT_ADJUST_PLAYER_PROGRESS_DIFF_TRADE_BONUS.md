---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_PROGRESS_DIFF_TRADE_BONUS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_PROGRESS_DIFF_TRADE_BONUS
>
> * Class: `PLAYERS`
> * Parameters:
>	* TechCivicsPerYield `Integer`

## Samples

```SQL {title="TRAIT_ADJUST_PROGRESS_DIFF_TRADE_BONUS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_ADJUST_PROGRESS_DIFF_TRADE_BONUS",
		"MODIFIER_PLAYER_ADJUST_PROGRESS_DIFF_TRADE_BONUS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_ADJUST_PROGRESS_DIFF_TRADE_BONUS",
		"TechCivicsPerYield",
		3
	);
	
```

