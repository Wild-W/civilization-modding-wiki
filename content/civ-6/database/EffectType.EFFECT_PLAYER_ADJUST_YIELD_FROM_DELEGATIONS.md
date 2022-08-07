---
tags:
- EffectType
title: EFFECT_PLAYER_ADJUST_YIELD_FROM_DELEGATIONS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_PLAYER_ADJUST_YIELD_FROM_DELEGATIONS
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Unknown`
>	* YieldType `Unknown`

## Samples

```SQL {title="DIPLOMATIC_QUARTER_DELEGATION_CULTURE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"DIPLOMATIC_QUARTER_DELEGATION_CULTURE",
		"MODIFIER_PLAYER_ADJUST_YIELD_FROM_DELEGATIONS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"DIPLOMATIC_QUARTER_DELEGATION_CULTURE",
		"Amount",
		1
	),
	(
		"DIPLOMATIC_QUARTER_DELEGATION_CULTURE",
		"YieldType",
		"YIELD_CULTURE"
	);
	
```

