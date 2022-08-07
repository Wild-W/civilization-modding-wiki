---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_YIELD_CHANGE_PER_GREAT_PERSON_CLASS_ON_RESOURCE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_YIELD_CHANGE_PER_GREAT_PERSON_CLASS_ON_RESOURCE
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Unknown`
>	* GreatPersonClassType `Unknown`
>	* ResourceType `Unknown`
>	* YieldType `Unknown`

## Samples

```SQL {title="HERMETIC_ORDER_GREAT_ARTIST_LEY_LINE_CULTURE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"HERMETIC_ORDER_GREAT_ARTIST_LEY_LINE_CULTURE",
		"MODIFIER_PLAYER_ADJUST_GREAT_PERSON_RESOURCE_YIELD_CHANGE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"HERMETIC_ORDER_GREAT_ARTIST_LEY_LINE_CULTURE",
		"Amount",
		1
	),
	(
		"HERMETIC_ORDER_GREAT_ARTIST_LEY_LINE_CULTURE",
		"GreatPersonClassType",
		"GREAT_PERSON_CLASS_ARTIST"
	),
	(
		"HERMETIC_ORDER_GREAT_ARTIST_LEY_LINE_CULTURE",
		"ResourceType",
		"RESOURCE_LEY_LINE"
	),
	(
		"HERMETIC_ORDER_GREAT_ARTIST_LEY_LINE_CULTURE",
		"YieldType",
		"YIELD_CULTURE"
	);
	
```

