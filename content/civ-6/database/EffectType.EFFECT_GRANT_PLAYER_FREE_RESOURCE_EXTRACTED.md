---
tags:
- EffectType
title: EFFECT_GRANT_PLAYER_FREE_RESOURCE_EXTRACTED
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_PLAYER_FREE_RESOURCE_EXTRACTED
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* ResourceType `String`

## Samples

```SQL {title="GREATPERSON_GRANT_1_COAL_PER_TURN"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GREATPERSON_GRANT_1_COAL_PER_TURN",
		"MODIFIER_PLAYER_ADJUST_FREE_RESOURCE_EXTRACTION",
		1,
		1
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GREATPERSON_GRANT_1_COAL_PER_TURN",
		"Amount",
		1
	),
	(
		"GREATPERSON_GRANT_1_COAL_PER_TURN",
		"ResourceType",
		"RESOURCE_COAL"
	);
	
```

