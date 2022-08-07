---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_GOLD_INTEREST_PERCENT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_GOLD_INTEREST_PERCENT
>
> * Class: `Unknown`
> * Parameters:
>	* Percent `Unknown`

## Samples
```SQL {title="GOVERNOR_PROMOTION_OWLS_OF_MINERVA_4_GOLD_INTEREST"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"GOVERNOR_PROMOTION_OWLS_OF_MINERVA_4_GOLD_INTEREST",
		"MODIFIER_PLAYER_ADJUST_GOLD_INTEREST_PERCENT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GOVERNOR_PROMOTION_OWLS_OF_MINERVA_4_GOLD_INTEREST",
		"Percent",
		3
	);
	
```

