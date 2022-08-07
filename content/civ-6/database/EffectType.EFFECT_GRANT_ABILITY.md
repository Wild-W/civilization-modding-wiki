---
tags:
- EffectType
title: EFFECT_GRANT_ABILITY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_ABILITY
>
> * Class: `UNITS`
> * Parameters:
>	* AbilityType `String`
>	* ModifierId `String`

## Samples
```SQL {title="MISSIONARY_ZEAL_IGNORE_TERRAIN_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MISSIONARY_ZEAL_IGNORE_TERRAIN_MODIFIER",
		"MODIFIER_PLAYER_UNITS_GRANT_ABILITY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MISSIONARY_ZEAL_IGNORE_TERRAIN_MODIFIER",
		"AbilityType",
		"ABILITY_RELIGIOUS_IGNORE_TERRAIN_COST"
	);
	
```

```SQL {title="GREATPERSON_MOVEMENT_AOE_INFORMATION_SEA"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"GREATPERSON_MOVEMENT_AOE_INFORMATION_SEA",
		"MODIFIER_PLAYER_UNITS_GRANT_ABILITY",
		"AOE_INFORMATION_SEA_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GREATPERSON_MOVEMENT_AOE_INFORMATION_SEA",
		"ModifierId",
		"ABILITY_GREAT_ADMIRAL_MOVEMENT"
	);
	
```

