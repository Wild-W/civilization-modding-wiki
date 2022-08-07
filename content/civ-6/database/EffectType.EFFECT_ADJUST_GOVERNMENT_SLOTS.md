---
tags:
- EffectType
title: EFFECT_ADJUST_GOVERNMENT_SLOTS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_GOVERNMENT_SLOTS
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Integer`
>	* GovernmentSlotType `String`

## Samples
```SQL {title="GOVT_ADD_WILDCARD_SLOT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"GOVT_ADD_WILDCARD_SLOT",
		"MODIFIER_GOVERNMENT_ADJUST_SLOTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GOVT_ADD_WILDCARD_SLOT",
		"Amount",
		1
	),
	(
		"GOVT_ADD_WILDCARD_SLOT",
		"GovernmentSlotType",
		"SLOT_WILDCARD"
	);
	
```

